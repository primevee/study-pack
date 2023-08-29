#include <stdio.h>
#include <stddef.h>
#include "lists.h"

/**
 * print_dlistint - print node values
 * @h: head of list
 *
 * Return: return number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *hold = NULL;
	size_t n = 0;

	if (!h)
		return (n);
	hold = (dlistint_t *) h;
	while (hold)
	{
		printf("%d\n", hold->n);
		hold = hold->next;
		n++;
	}

	return (n);
}
