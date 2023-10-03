class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LENGTH = 5
VALID_DOMAINS = ['.com', '.bg', '.net', '.org']

while True:
    command = input()
    if command == 'End':
        break

    if '@' not in command:
        raise MustContainAtSymbolError('Email must contain @')

    if len(command.split('@')[0]) < EMAIL_MIN_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')

    domain = '.' + command.split('.')[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
