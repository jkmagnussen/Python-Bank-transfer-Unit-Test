 #Bank Accont transfer
#Joseph Karl Magnussen - Student ID: H00069811
# Module: CKIT-535 Week 3 - Individual Assignment - Unit Testing

import unittest
import Bank_transfer_programme as btp

class KnownValues (unittest.TestCase):
    def test_acceptable_transfer(self):
        savings_account = btp.account(200)
        Cheq_acc = btp.account(0)
        savings_account.transfer(75, Cheq_acc)
        self.assertEqual(savings_account.balance, 125)
        self.assertEqual(Cheq_acc.balance, 75)

    def test_wrong_transfer (self):
        savings_account = btp.account(200)
        Cheq_acc = btp.account(0)
        savings_account.transfer(1000, Cheq_acc)
        self.assertEqual(savings_account.balance, 200)
        self.assertEqual(Cheq_acc.balance, 0)

    def test_exact_transfer (self):
        savings_account = btp.account(200)
        Cheq_acc = btp.account(0)
        savings_account.transfer(200, Cheq_acc)
        self.assertEqual(savings_account.balance, 0)
        self.assertEqual(Cheq_acc.balance, 200)

    def test_negative_transfer (self):
        savings_account = btp.account(200)
        Cheq_acc = btp.account(0)
        savings_account.transfer(-200, Cheq_acc)
        self.assertEqual(savings_account.balance, 200)
        self.assertEqual(Cheq_acc.balance, 0)

if __name__ == '__main__':
    unittest.main()
