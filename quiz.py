from cryptography.fernet import Fernet

Key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABc9aIIGsnT2BSgNm1rH5uAi_FQOZYt3WeHQSQBgisWgSXmqdrHt580JIPjxHH75BO1a0iQNBUHjIkByMM_a3kXCDK6KWd_49LGbLKzzxVRRttoTHWkK3d5kvw3j7JAfUwTPFPJjN_IRyl1QC9DP8AwKn4iYZi6RNvcVuXudouMU9n_tZU='

def main():
    f = Fernet(Key)
    print(f.decrypt(message))


if __name__ != "__name__":
    main()