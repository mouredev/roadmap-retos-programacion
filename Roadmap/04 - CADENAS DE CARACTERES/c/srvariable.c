/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

#define MSG1 "Hola Mundo, esto es C."
#define MSG2 "Mundo"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void	ft_strtoupper(char *str);
void	ft_strtolower(char *str);
char	*ft_strjoin(const char *s1, const char *s2);
char	**ft_split(const char *s1, char delim);
void	ft_freesplit(char ***split);
int		is_palindrome(const char *s1);
int		is_anagram(const char *s1, const char *s2);
int		is_isogram(const char *s1);

int	main(void)
{
	/* === 1 === */
	char	s1[100] = MSG1;
	char	s2[100] = MSG2;
	char	*ret = NULL;
	int		ret2 = 0;
	char	**ret3 = NULL;

	printf("\nAplicando stpcpy, para copiar s2 a s1\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret = stpcpy(s1, s2);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	printf("stpcpy devuelve un puntero al final de s1\n");
	printf("Dirección de memoria de s1: %p\n", s1);
	printf("Dirección de memoria de ret: %p\n", ret);

	printf("\nRestaurando los valores originales...\n");
	stpcpy(s1, MSG1);
	ret= NULL;

	printf("\nAplicando strcat, para concatenar s2 a s1\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret = strcat(s1, s2);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	printf("strcat devuelve un puntero al inicio de s1\n");
	printf("Dirección de memoria de s1: %p\n", s1);
	printf("Dirección de memoria de ret: %p\n", ret);

	printf("\nRestaurando los valores originales...\n");
	stpcpy(s1, MSG1);
	ret = NULL;

	printf("\nAplicando strchr, para encontrar la primera ocurrencia de 'a' en s1\n");
	printf("Antes -> s1: %s, ret: %s\n", s1, ret);
	ret = strchr(s1, 'a');
	printf("Después -> s1: %s, ret: %s\n", s1, ret);
	printf("strchr devuelve un puntero a la primera ocurrencia\n");
	printf("Dirección de memoria de s1: %p\n", s1);
	printf("Dirección de memoria de ret: %p\n", ret);

	printf("\nRestaurando los valores originales...\n");
	stpcpy(s1, MSG1);
	ret = NULL;

	printf("\nAplicando strcmp, para comparar s1 y s2\n");
	printf("Antes -> s1: %s, s2: %s, ret2: %d\n", s1, s2, ret2);
	ret2 = strcmp(s1, s2);
	printf("Después -> s1: %s, s2: %s, ret2: %d\n", s1, s2, ret2);
	printf("strcmp devuelve la diferencia entre el primer byte diferente\n");
	printf("o 0 si son iguales\n");

	printf("\nRestaurando los valores originales...\n");
	ret2 = 0;

	printf("\nAplicando strcpy, para copiar s2 a s1\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret = strcpy(s1, s2);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	printf("strcpy devuelve un puntero al inicio de s1\n");
	printf("Dirección de memoria de s1: %p\n", s1);
	printf("Dirección de memoria de ret: %p\n", ret);

	printf("\nRestaurando los valores originales...\n");
	stpcpy(s1, MSG1);
	ret = NULL;

	printf("\nAplicando strcspn, para obtener el tamaño de bytes en s1 que no están en s2\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret2 = strcspn(s1, s2);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	printf("strcspn devuelve el número de bytes de s1 que no están en s2\n");

	printf("\nRestaurando los valores originales...\n");
	ret2 = 0;

	printf("\nAplicando strdup, para obtener un duplicado de un string\n");
	printf("Antes -> s1: %s, ret: %s\n", s1, ret);
	ret = strdup(s1);
	if (!ret) return (1);
	printf("Después -> s1: %s, ret: %s\n", s1, ret);
	printf("strdup devuelve una copia de s1, con memoria asignada usando malloc\n");
	printf("o NULL si falla\n");
	printf("Es importante hacer free de la copia, para evitar fugas de memoria\n");
	printf("Dirección de memoria de s1: %p\n", s1);
	printf("Dirección de memoria de ret: %p\n", ret);

	printf("\nRestaurando los valores originales...\n");
	free(ret);
	ret = NULL;

	printf("\nAplicando strlen, para obtener el tamaño de s1\n");
	printf("Antes -> s1: %s, ret2: %d\n", s1, ret2);
	ret2 = strlen(s1);
	printf("Después -> s1: %s, ret2: %d\n", s1, ret2);
	printf("strlen devuelve el tamaño de s1\n");

	printf("\nRestaurando los valores originales...\n");
	ret2 = 0;

	printf("\nAplicando strncat, para concatenar 2 bytes de s2 a s1\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret = strncat(s1, s2, 2);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	printf("strncat devuelve un puntero a s1\n");
	printf("Dirección de memoria de s1: %p\n", s1);
	printf("Dirección de memoria de ret: %p\n", ret);

	printf("\nRestaurando los valores originales...\n");
	stpcpy(s1, MSG1);

	printf("\nAplicando strncmp, para comparar 2 bytes de s2 a s1\n");
	printf("Antes -> s1: %s, s2: %s, ret2: %d\n", s1, s2, ret2);
	ret2 = strncmp(s1, s2, 2);
	printf("Después -> s1: %s, s2: %s, ret2: %d\n", s1, s2, ret2);
	printf("strncmp devuelve la diferencia entre el primer byte diferente\n");

	printf("\nRestaurando los valores originales...\n");
	ret2 = 0;

	printf("\nAplicando strpbrk, para comparar 2 bytes de s2 a s1\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret = strpbrk(s1, s2);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	printf("strpbrk devuelve un puntero al primer byte en s1 que haya en s2\n");
	printf("o NULL si no lo encuentra\n");

	printf("\nRestaurando los valores originales...\n");
	ret = NULL;

	printf("\nAplicando strrchr, para encontrar la última ocurrencia de 'a' en s1\n");
	printf("Antes -> s1: %s, ret: %s\n", s1, ret);
	ret = strrchr(s1, 'a');
	printf("Después -> s1: %s, ret: %s\n", s1, ret);
	printf("strrchr devuelve un puntero a la última ocurrencia\n");
	printf("o NULL si no lo encuentra\n");

	printf("\nRestaurando los valores originales...\n");
	ret = NULL;

	char	*s3 = strdup("Va,a,eliminar.todos los separadores");
	if (!s3) return (2);
	char	*temp = s3;
	char	*delim = ",. ";
	printf("\nAplicando strsep, para encontrar uno de los bytes de delim en s3\n");
	printf("Antes -> s3: %s, delim: %s, ret: %s\n", s3, delim, ret);
	ret = strsep(&s3, delim);
	while (ret)
	{
		printf("Después -> s3: %s, delim: %s, ret: %s\n", s3, delim, ret);
		ret = strsep(&s3, delim);
	}
	printf("strsep devuelve el string hasta el primer byte de delim que encuentre en s3\n");
	printf("o NULL si no lo encuentra\n");
	printf("NOTA: Modifica el puntero, así que si tiene memoria alojada, recuerda ");
	printf("tener un puntero al primer byte para poder liberarlo posteriormente\n");

	printf("\nRestaurando los valores originales...\n");
	free(temp);
	s3 = NULL;
	temp = NULL;
	ret = NULL;

	printf("\nAplicando strstr, buscar s2 en s1\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret = strstr(s1, s2);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	printf("strstr devuelve un puntero al inicio del s2 en s1 si lo encuentra ");
	printf("o NULL si no lo encuentra\n");

	printf("\nRestaurando los valores originales...\n");
	ret = NULL;

	printf("\nAplicando strstr, buscar s2 en s1\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret = strstr(s1, s2);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	printf("strstr devuelve un puntero al inicio del s2 en s1 si lo encuentra ");
	printf("o NULL si no lo encuentra\n");

	printf("\nRestaurando los valores originales...\n");
	ret = NULL;

	printf("\nRestaurando los valores originales...\n");
	ret = NULL;

	s3 = strdup("Va,a,eliminar.todos los separadores");
	if (!s3) return (3);
	temp = s3;
	printf("\nAplicando strtok, para encontrar uno de los bytes de delim en s3\n");
	printf("Antes -> s3: %s, delim: %s, ret: %s\n", s3, delim, ret);
	ret = strtok(s3, delim);
	while (ret)
	{
		printf("Después -> s3: %s, delim: %s, ret: %s\n", s3, delim, ret);
		ret = strtok(NULL, delim);
	}
	printf("strtok devuelve el string hasta el primer byte de delim que encuentre en s3\n");
	printf("o NULL si no lo encuentra\n");
	printf("La primera vez el primer parámetro tiene que ser string y las siguientes ");
	printf("tiene que ser NULL\n");
	printf("NOTA: Modifica el puntero, así que si tiene memoria alojada, recuerda ");
	printf("tener un puntero al primer byte para poder liberarlo posteriormente\n");

	printf("\nRestaurando los valores originales...\n");
	free(temp);
	s3 = NULL;
	temp = NULL;
	ret = NULL;

	/* === BONUS === */
	s3 = strdup("Increible me voy a volver mayuscula.");
	if (!s3) return (4);
	printf("\nAplicando ft_strtoupper para convertir el string en mayúsculas\n");
	printf("Antes -> s3: %s\n", s3);
	ft_strtoupper(s3);
	printf("Después -> s3: %s\n", s3);

	printf("\nRestaurando los valores originales...\n");
	free(s3);
	s3 = NULL;

	s3 = strdup("INCREIBLE ME VOY A VOLVER MINUSCULA.");
	if (!s3) return (5);
	printf("\nAplicando ft_strtolower para convertir el string en minúsculas\n");
	printf("Antes -> s3: %s\n", s3);
	ft_strtolower(s3);
	printf("Después -> s3: %s\n", s3);

	printf("\nRestaurando los valores originales...\n");
	free(s3);
	s3 = NULL;

	printf("\nAplicando ft_strjoin para unir s1 y s2\n");
	printf("Antes -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);
	ret = ft_strjoin(s1, s2);
	if (!ret) return (6);
	printf("Después -> s1: %s, s2: %s, ret: %s\n", s1, s2, ret);

	printf("\nRestaurando los valores originales...\n");
	free(ret);
	ret = NULL;

	printf("\nAplicando ft_split para separar un s1 por espacios\n");
	printf("Antes -> s1: %s\n", s1);
	if (!ret3) printf("ret3: NULL\n");
	ret3 = ft_split(s1, ' ');
	if (!ret3) return (7);
	printf("Después s1: %s, ", s1);
	for (int i = 0; ret3[i]; ++i)
	{
		if (ret3[i + 1]) printf("ret3[%d]: %s, ", i, ret3[i]);
		else printf("ret3[%d]: %s\n", i, ret3[i]);
	}
	ft_freesplit(&ret3);

	/* === DIFICULTAD EXTRA === */
	const char	*word1 = "Ojo rojo";
	const char	*word2[2] = {"topar", "potar"};
	const char	*word3 = "baba";

	if (is_palindrome(word1)) printf("%s es palíndromo\n", word1);
	else printf("%s no es palíndromo\n", word1);
	if (is_palindrome(word2[0])) printf("%s es palíndromo\n", word2[0]);
	else printf("%s no es palíndromo\n", word2[0]);
	if (is_palindrome(word2[1])) printf("%s es palíndromo\n", word2[1]);
	else printf("%s no es palíndromo\n", word2[1]);
	if (is_palindrome(word3)) printf("%s es palíndromo\n", word3);
	else printf("%s no es palíndromo\n", word3);

	if (is_anagram(word1, word1)) printf("%s es anagrama de %s\n", word1, word1);
	else printf("%s no es anagrama de %s\n", word1, word1);
	if (is_anagram(word2[0], word2[1])) printf("%s es anagrama de %s\n", word2[0], word2[1]);
	else printf("%s no es anagrama de %s\n", word2[0], word2[1]);
	if (is_anagram(word2[1], word2[1])) printf("%s es anagrama de %s\n", word2[1], word2[1]);
	else printf("%s no es anagrama de %s\n", word2[1], word2[1]);
	if (is_anagram(word3, word1)) printf("%s es anagrama de %s\n", word3, word1);
	else printf("%s no es anagrama de %s\n", word3, word1);
	if (is_anagram("Hola", "hola")) printf("%s es anagrama de %s\n", "hola", "hola");
	else printf("%s no es anagrama de %s\n", "hola", "hola");

	if (is_isogram(word1)) printf("%s es isograma\n", word1);
	else printf("%s no es isograma\n", word1);
	if (is_isogram(word2[0])) printf("%s es isograma\n", word2[0]);
	else printf("%s no es isograma\n", word2[0]);
	if (is_isogram(word2[1])) printf("%s es isograma\n", word2[1]);
	else printf("%s no es isograma\n", word2[1]);
	if (is_isogram(word3)) printf("%s es isograma\n", word3);
	else printf("%s no es isograma\n", word3);
	return (0);
}

void	ft_strtoupper(char *str)
{
	size_t	index;
	if (!str) return;

	index = 0;
	while (str[index])
	{
		str[index] = toupper(str[index]);
		++index;
	}
}

void	ft_strtolower(char *str)
{
	size_t	index;
	if (!str) return;

	index = 0;
	while (str[index])
	{
		str[index] = tolower(str[index]);
		++index;
	}
}

// Esta implementación de strlen es para evitar segfaults
// cuando el string es NULL.
static size_t	ft_strlen(const char *s)
{
	int	counter;

	if (!s) return (0);
	counter = 0;
	while (s[counter])
		++counter;
	return (counter);
}

char	*ft_strjoin(const char *s1, const char *s2)
{
	size_t	len1;
	size_t	len2;
	char	*ret;

	len1 = ft_strlen(s1);
	len2 = ft_strlen(s2);
	ret = (char *)malloc((len1 + len2 + 1) * sizeof(char));
	if (!ret) return (NULL);
	ret[len1 + len2] = '\0';
	while (len2--)
		ret[len1 + len2] = s2[len2];
	while (len1--)
		ret[len1] = s1[len1];
	return (ret);
}

void	ft_freesplit(char ***split)
{
	size_t	index;

	if (!(*split)) return;
	index = 0;
	while ((*split)[index])
	{
		free((*split)[index]);
		(*split)[index] = NULL;
		++index;
	}
	free(*split);
	*split = NULL;
}

static size_t	count_word(const char *str, char delimit)
{
	size_t	counter;
	size_t	index;

	if (!str)
		return (0);
	counter = 0;
	index = 0;
	while (str[index])
	{
		if (str[index] == delimit)
			++index;
		else
		{
			++counter;
			while (str[index] && str[index] != delimit)
				++index;
		}
	}
	return (counter);
}

static char	*get_word(const char *str, char delimit, size_t *index)
{
	char	*word;
	size_t	index2;

	index2 = 0;
	while (str[*index + index2] && str[*index + index2] != delimit)
		++index2;
	word = (char *)malloc((index2 + 1) * sizeof(char));
	if (!word)
		return (NULL);
	index2 = 0;
	while (str[*index] && str[*index] != delimit)
	{
		word[index2] = str[*index];
		++index2;
		++(*index);
	}
	word[index2] = '\0';
	return (word);
}

char	**ft_split(const char *str, char delimit)
{
	char	**split;
	size_t	split_index;
	size_t	str_index;

	if (!str) return (NULL);
	split = (char **)malloc((count_word(str, delimit) + 1) * sizeof(char *));
	if (!split) return (NULL);
	split_index = 0;
	str_index = 0;
	while (str[str_index])
	{
		if (str[str_index] == delimit)
			++str_index;
		else
		{
			split[split_index] = get_word(str, delimit, &str_index);
			if (!split[split_index])
			{
				ft_freesplit(&split);
				return (NULL);
			}
			++split_index;
		}
	}
	split[split_index] = NULL;
	return (split);
}

int		is_palindrome(const char *s1)
{
	size_t	length;
	char	**split;
	char	*join;
	char	*temp;

	if (!s1 || !(*s1)) return (0);
	split = ft_split(s1, ' ');
	if (!split) return (0);
	join = NULL;
	for (size_t i = 0; split[i]; ++i)
	{
		temp = ft_strjoin(join, split[i]);
		if (!temp)
		{
			ft_freesplit(&split);
			free(join);
			return (0);
		}
		free(join);
		join = strdup(temp);
		if (!join)
		{
			ft_freesplit(&split);
			free(temp);
			return (0);
		}
		free(temp);
	}
	ft_freesplit(&split);
	ft_strtolower(join);
	length = strlen(join);
	for (size_t i = 0; i < length; ++i)
	{
		if (join[i] != join[length - 1 - i])
		{
			free(join);
			return (0);
		}
	}
	free(join);
	return (1);
}

int		is_anagram(const char *s1, const char *s2)
{
	int		counter[2][26] = {0};
	char	*temp[2];

	if (!s1 || !s2) return (0);
	temp[0] = strdup(s1);
	if (!temp[0]) return (0);
	temp[1] = strdup(s2);
	if (!temp[1])
	{
		free(temp[0]);
		return (0);
	}
	ft_strtolower(temp[0]);
	ft_strtolower(temp[1]);
	for (size_t i = 0; temp[0][i]; ++i)
		if (isalpha(s1[i])) ++counter[0][temp[0][i] - 'a'];
	for (size_t i = 0; temp[1][i]; ++i)
		if (isalpha(s2[i])) ++counter[1][temp[1][i] - 'a'];
	for (size_t i = 0; i < 26; ++i)
	{
		if (counter[0][i] != counter[1][i])
		{
			free(temp[0]);
			free(temp[1]);
			return (0);
		}
	}
	free(temp[0]);
	free(temp[1]);
	return (1);
}

int		is_isogram(const char *s1)
{
	int		counter[26] = {0};
	int		amount;
	char	*temp;

	if (!s1) return (0);
	temp = strdup(s1);
	if (!temp) return (0);
	ft_strtolower(temp);
	for (size_t i = 0; temp[i]; ++i)
		if (isalpha(temp[i])) ++counter[temp[i] - 'a'];
	amount = 0;
	for (size_t i = 0; i < 26; ++i)
	{
		if (!counter[i]) continue;
		if (!amount) amount = counter[i];
		else if (amount != counter[i])
		{
			free(temp);
			return (0);
		}
	}
	free(temp);
	return (1);
}
