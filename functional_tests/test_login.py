from django.core import mail
from selenium.webdriver.common.keys import Keys
import re
from .base import FunctionalTest
import os
import time
import os
import poplib
import re
import time


TEST_EMAIL = os.environ.get('TEST_EMAIL')
SUBJECT = "Your login link for Superlists"

if TEST_EMAIL == "" or TEST_EMAIL is None:
    print("Set the TEST_EMAIL environment variable to the recipient!")
    exit(-1)


class LoginTest(FunctionalTest):
    def wait_for_email(self, test_email, subject):
        if not self.staging_server:
            email = mail.outbox[0]
            self.assertIn(test_email, email.to)
            self.assertEqual(email.subject, subject)
            return email.body

        email_id = None
        end_time = time.time() + 300
        try:
            while time.time() < end_time:
                inbox = poplib.POP3_SSL('pop.gmail.com')
                inbox.user(test_email)
                inbox.pass_(os.environ['TEST_EMAIL_PASSWORD'])
                # get 10 newest messages
                print("Getting mailbox statistics")
                count, _ = inbox.stat()
                print("Message count:", count)
                for i in reversed(range(max(1, count - 10), count+1)):
                    print('getting msg', i)
                    _, lines, __ = inbox.retr(i)
                    lines = [l.decode('utf8') for l in lines]
                    print(lines)
                    if f'Subject: {subject}' in lines:
                        email_id = i
                        body = '\n'.join(lines)
                        return body
                time.sleep(10)
                inbox.quit()
        finally:
            if email_id:
                print("Deleting email with ID:",i)
                inbox.dele(email_id)
            inbox.quit()

    def test_can_get_email_link_to_log_in(self):
        # Edith goes to the awesome superlists site
        # and notices a "Log In" section in the navbar for the first time
        # It's telling her to enter her email address, so she does
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # A message appears telling her an email has been sent
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))

        # She checks her email and finds a message
        body = self.wait_for_email(TEST_EMAIL, SUBJECT)

        # It has a url link in it
        print("Email body",body)
        self.assertIn('Use this link to log in', body)
        url_search = re.search(r'http://.+/.+$', body)
        if not url_search:
            self.fail(f'Could not find url in email body:\n{body}')
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # She clicks it
        self.browser.get(url)

        # she is logged in!
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # Now she logs out
        self.browser.find_element_by_link_text('Log out').click()

        # She is logged out
        self.wait_to_be_logged_out(email=TEST_EMAIL)

