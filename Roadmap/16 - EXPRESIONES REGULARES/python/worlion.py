import unittest
import re

"""
 * EJERCICIO: REGEX
"""

def extract_numbers(text: str) -> str:
    regex = "\d+"
    return re.findall(regex, txt)

txt = "mi perro tiene 6 años y pesa 150kg., me lo compré el 7 de mayo al lado del 12 de octubre"

# print(f"Texto: {txt}")
# print(f"Numeros en el texto: {extract_numbers(txt)}")


"""
 * DIFICULTAD EXTRA (opcional):
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

rgx_digit = "\d+"
rgx_mail = "[a-zA-Z0-9]+[a-zA-Z0-9.-]*@[a-zA-Z0-9]+[a-zA-Z0-9]*.[a-zA-Z]+"
rgx_phone = "((\+|00)\d{1,3})?\d{9}"
rgx_url = "(http://|https://)?[a-z0-9]+([\-\.][a-z0-9]+)*\.[a-z]{2,}$"

def valid(text: str, regex: str) -> bool:
    print(f"validating '{text}' with '{regex}' : --> {bool(re.fullmatch(regex, text))}")
    return bool(re.fullmatch(regex, text))

def is_valid_number(number: str) -> bool:
    return valid(number, rgx_digit)

def is_valid_mail(mail: str) -> bool:
    return valid(mail, rgx_mail)

def is_valid_phone(phone: str) -> bool:
    # Descartamos los espacios
    return valid(phone.replace(' ', ''), rgx_phone)

def is_valid_url(url: str) -> bool:
    return valid(url, rgx_url)

class TestRegex(unittest.TestCase):
    
    def test_mail(self):
        print ("\nTest de mails:")
        self.assertTrue(is_valid_mail('imanol@pepe.com'))
        self.assertTrue(is_valid_mail('imanol-dev@pepe.com'))
        self.assertTrue(is_valid_mail('imanol.dev@pepe.com'))
        
        self.assertFalse(is_valid_mail('imanolpepe.com'))
        self.assertFalse(is_valid_mail('-imanol@pepe.com'))
    
    def test_phone(self):
        print ("\nTest de teléfonos:")
        self.assertTrue(is_valid_phone('666555444'))
        self.assertTrue(is_valid_phone('+34666555444'))
        self.assertTrue(is_valid_phone('+34 666 55 54 44'))
        self.assertFalse(is_valid_phone('-1666555444'))
        self.assertFalse(is_valid_phone('+9999999999999999999999999999666555444'))
        self.assertFalse(is_valid_phone('A 666 55 54 44'))
        
    def test_url(self):
        print ("\nTest de URLs:")
        self.assertTrue(is_valid_url('www.worlion.com'))
        self.assertTrue(is_valid_url('http://www.worlion.com'))
        self.assertTrue(is_valid_url('https://www.worlion.com'))
        self.assertTrue(is_valid_url('www.worlion-willenthur.com'))
        self.assertTrue(is_valid_url('worlion.com'))
        
        self.assertFalse(is_valid_url('www.worlion.com/'))
        self.assertFalse(is_valid_url('worlioncom'))
        self.assertFalse(is_valid_url('worlioncom'))
        self.assertFalse(is_valid_url('httpa://www.worlion.com'))
        self.assertFalse(is_valid_url('www.worlion..com'))
        
        
if __name__ == '__main__':
    unittest.main()
    
