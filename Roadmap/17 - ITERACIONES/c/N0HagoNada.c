#include <stdio.h>

int main()
{
    // Primera forma
    for (int i = 1; i <= 10; i++)
    {
        printf("%d\n", i);
    }
    // Segunda forma
    int i = 1;
    while (i <= 10)
    {
        printf("%d\n", i);
        i++;
    }
    // Tercera forma
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", nums[i]);
    }
    return 0;
}