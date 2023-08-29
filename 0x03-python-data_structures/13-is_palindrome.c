#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if linked lis is palindrome
 * @head: pointer to head of liked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int buf[1024], i = 0, j = 0, len = 0, hold;

	if (!head || !*head)
		return (0);
	current = *head;
	for (; current; i++)
	{
		buf[i] = current->n;
		current = current->next;
	}
	len = i;
	i--;
	for (; j < len; j++, i--)
	{
		hold = buf[j] - buf[i];
		if (hold)
			return (0);
	}
	return (1);
}
