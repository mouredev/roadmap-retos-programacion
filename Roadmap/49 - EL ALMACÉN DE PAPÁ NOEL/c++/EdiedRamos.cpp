// * EdiedRamos

#include <iostream>
#include <time.h>
#include <stdlib.h>

using namespace std;

#define OPTIONS {'A', 'B', 'C', '1', '2', '3'}

const int codeLength = 4;

string createCode()
{
  string code = "";

  char options[] = OPTIONS;
  const int optionsLength = sizeof(options) / sizeof(options[0]);

  srand(time(NULL));
  for (int i = optionsLength - 1; i > 0; i--)
  {
    int random = rand() % (i + 1);
    swap(options[i], options[random]);
  }

  for (int i = 0; i < codeLength; i++)
    code += options[i];

  return code;
}

char toUpper(char c)
{
  return c >= 'a' && c <= 'z' ? c & 0x5F : c;
}

void toUpper(string &s)
{
  for (char &c : s)
    c = toUpper(c);
}

bool isCorrectFormat(string code)
{
  if (code.size() != codeLength)
    return false;

  char options[] = OPTIONS;
  bool characterExists;
  for (char codeCharacter : code)
  {
    characterExists = false;
    for (char optionCharacter : options)
      if (toUpper(codeCharacter) == optionCharacter)
      {
        characterExists = true;
        break;
      }
    if (!characterExists)
      return false;
  }

  return true;
}

bool contains(string a, char b)
{
  for (char c : a)
    if (c == b)
      return true;
  return false;
}

void start()
{
  const string secretCode = createCode();
  const int maxAttempts = 10;
  int attempts = 1;
  string userCode = "";
  bool codeChecked;
  while (attempts <= maxAttempts)
  {
    codeChecked = false;
    cout << "Intento #" << attempts << endl;
    while (!codeChecked)
    {
      cout << "Ingrese un código de 4 caracteres utilizando [ABC123]:";
      getline(cin, userCode);
      codeChecked = isCorrectFormat(userCode);
      if (!codeChecked)
        cout << "El código ingresado no cumple el formato" << endl;
    }
    toUpper(userCode);

    if (userCode == secretCode)
    {
      cout << "Código encontrado en " << attempts << " intentos." << endl;
      break;
    }

    for (int i = 0; i < codeLength; i++)
    {
      cout << userCode[i] << ": ";
      if (secretCode[i] == userCode[i])
        cout << "Correcto" << endl;
      else if (contains(secretCode, userCode[i]))
        cout << "Presente" << endl;
      else
        cout << "Incorrecto" << endl;
    }

    attempts++;
  }

  if (attempts > maxAttempts)
    cout << "El código no fue encontrado" << endl;
}

int main()
{
  start();
  return 0;
}