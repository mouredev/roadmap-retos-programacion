#include <iostream>
#include <cstring>

#define MAX_SIZE 50

int Longitud(char word[])
{
    int i = 0;

    while(*word)
    {
        i++;
        word++;
    }

    return i;
}

bool EsPalindronmo(char word[])
{
    bool check = true;
    int size = Longitud(word);
    char first = word[0];
    char last = word[size-1];

    for(int i=0; i<size/2; i++)
    {
        if(first != last)
        {
            check = false;
            break;
        }
        else
        {
            first = word[i];
            last = word[size-1-i];
        }
    }

    return check;
}

bool SonAnagramas(char wordA[], char wordB[])
{
    bool check = true;
    bool charCheck;
    int sizeA = Longitud(wordA);
    int sizeB = Longitud(wordB);

    if(sizeA != sizeB)
        check = false;
    else
    {
        for(int i=0; i<sizeA; i++)
        {
            charCheck = false;

            for(int j=0; j<sizeB; j++)
            {
                if(wordA[i] == wordB[j])
                {
                    charCheck = true;
                    break;
                }
            }

            if(!charCheck)
                break;
        }
    }    

    return (check and charCheck);
}

bool EsIsograma(char word[])
{
    bool check = true;
    int size = Longitud(word);

    for(int i=0; i<size; i++)
    {
        for(int j=(i+1); j<size; j++)
        {
            if(word[i] == word[j])
            {
                check = false;
                break;
            }
        }

        if(!check)
            break;
    }

    return check;
}

int main()
{
    // - - - PALÍNDROMOS - - -
    char word[MAX_SIZE];
    printf("Ingrese una palabra para saber si es un palindromo: ");
    scanf("%s", &word);
    if(EsPalindronmo(word))
    printf("La palabra %s es un palindromo\n", word);
    else
    printf("La palabra %s no es un palindromo\n", word);
    
    // - - - ANAGRAMAS - - -
    char wordA[MAX_SIZE], wordB[MAX_SIZE];
    printf("Ingrese una palabra: ");
    scanf("%s", &wordA);
    printf("Ingrese otra palabra para saber si es un anagrama de %s: ", wordA);
    scanf("%s", &wordB);
    if(SonAnagramas(wordA, wordB))
    printf("Las palabras %s y %s son anagramas.\n", wordA, wordB);
    else
    printf("Las palabras %s y %s no son anagramas.\n", wordA, wordB);

    // - - - ISOGRAMAS - - -
    char wordC[MAX_SIZE];
    printf("Ingrese una palabra para saber si es un isograma: ");
    scanf("%s", &wordC);
    if(EsIsograma(wordC))
    printf("La palabra %s es un isograma\n", wordC);
    else
    printf("La palabra %s no es un isograma\n", wordC);

    printf("Fin del programa.\n");
    
    return 0;
}