#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - Checks if it is a palindrome
  * @head: The head
  *
  * Return: 1 if it is a palindrome and 0 if it isn't
  */
int is_palindrome(listint_t **head)
{
    listint_t *start = NULL, *end = NULL;
    unsigned int x = 0, length = 0, cyc = 0, list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    start = *head;
    length = listint_len(start);
    cyc = length * 2;
    list = cyc - 2;
    end = *head;

    for (; x < cyc; x = x + 2)
    {
        if (start[x].n != end[list].n)
            return (0);

        list = list - 2;
    }

    return (1);
}

/**
  * get_node_at_index - gets a node from the list
  * @head: the head
  * @index: the index
  *
  * Return: the node of the linked list
  */
listint_t *get_node_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iterations = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (iterations == index)
				return (current);

			current = current->next;
			++iterations;
		}
	}

	return (NULL);
}

/**
  * slistint_len - number of elements counter
  * @h: the linked list to be counted
  *
  * Return: number of elements
  */
size_t listint_len(const listint_t *h)
{
	int len = 0;

	while (h != NULL)
	{
		++len;
		h = h->next;
	}

	return (len);
}
