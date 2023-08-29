#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node into linked list
 * @head: pointer to head of node
 * @number: number to be inserted
 *
 * Return: pointer to new node on success NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *previous_node;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	current_node = *head;
	previous_node = NULL;

	while (current_node && current_node->n < number)
	{
		previous_node = current_node;
		current_node = current_node->next;
	}

	if (!previous_node)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		previous_node->next = new_node;
		new_node->next = current_node;
	}

	return (new_node);
}
