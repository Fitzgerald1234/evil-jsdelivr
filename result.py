# uncompyle6 version 3.5.0
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.5 (default, Jun 28 2022, 15:30:04) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: RandomTeaParty.py
import argparse, hashlib

class LCG(object):

    def __init__(self, seed, p, a, c):
        self.p = p
        self.seed = seed
        self.a = a
        self.c = c

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.p
        return self.seed


encrypted_secret = [
 365568652,
 495714267,
 1358608273,
 1529160966,
 822619654,
 1706526019,
 391137561,
 2076472716,
 1764278540,
 734807837,
 2073337261,
 736054556,
 2123830086,
 681801730,
 1070017952,
 1709297869,
 1046640222,
 667366781,
 58152428,
 310139563,
 640852461,
 85665152,
 1240055427,
 1907395889,
 695586467,
 750761920,
 1239683690,
 1137452295,
 1250976842,
 808635844,
 1000374841,
 777628850,
 1057483327,
 89023171,
 121647634,
 837428821,
 1438310703,
 548816510,
 558030123,
 788206776,
 562475864,
 634461615,
 834403405,
 1433232113,
 209086350,
 1784777833,
 258061229,
 1469928947,
 2076352416,
 252437757,
 598438083,
 1401155011]

def print_hint():
    print('"Indeed, Perhaps you might want one, but its not going to be as easy as looking at the code!" said the March Hare')
    super_hard_to_find_hint_that_is_definitely_not_here = 'Vm10V1YxUXhUa1ppUldocFUwaENTMVZ1Y0VaTlZrNVdXa2RHYUZJeFNqQlVNV2h6WVVaa1IxTnVUbFJXVjJoTVdWVmtTMlJHVm5WWGJXeFdUVVphZFZkV1dtOVZNbFp5WWtWb1ZtSllhR2haYkdRMFRWWnNWMkZHVG1wTmJGcFZWVmR3UjJGWFNsWmpSRlpZWWtkU1NGa3llSE5YUms1MVZHMUdWazFHVlRVPQ=='


def main():
    parser = argparse.ArgumentParser('Random Tea Party', description='Welcome to the random tea party! hosted by yours truly, the Random Hatter!')
    parser.add_argument('--can-i-get-a-hint-please', default=False, action='store_true', help='There is no shame in asking for some help!')
    args = parser.parse_args()
    if args.can_i_get_a_hint_please:
        print_hint()
        return
    print("'I haven't the slightest idea,' said the Random Hatter.")
    print("'Nor I,' said the March Hare. After a long pause the Random Hatter decided to challange me with a second riddle")
    print(f"'I have {len(encrypted_secret)} favorite random numbers, can you guess them all?' he said, with a sinister smile on his face")
    secret = []
    for i, enc in enumerate(encrypted_secret):
        guess = int(input(f"My #{i} favorite number is? "))
        decrypted = chr((enc ^ guess) % 255)
        if not (i == 0 and decrypted == 'd' and i == 1 and decrypted == 'i' and i == 2 and decrypted == 'd' and i == 3 and decrypted == ' ' and i == 4 and decrypted == 'y' and i == 5 and decrypted == 'o' and i == 6 and decrypted == 'u'):
            print('Wrong!')
            return
        secret.append(decrypted)

    if hashlib.sha256(''.join(secret).encode()).hexdigest() == '0ecc299684a6063fabd161ac4ee3652195f567c799fccf44c09bf41e97d58288':
        print('Impressive, ' + ''.join(secret))
    else:
        print('Wrong!')


if __name__ == '__main__':
    main()
