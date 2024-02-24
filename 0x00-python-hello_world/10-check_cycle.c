#include "lists.h"

/**
 * check_cycle - function checks for a cycle in a singly linked list.
 * @list: pointer to the node beginning
 * Return: 0 if no cycle and 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *cur, *checker;

	if (list == NULL || list->next == NULL)
		return (0);
	cur = list;
	checker = cur->next;

	while (cur != NULL && checker->next != NULL
		&& checker->next->next != NULL)
	{
		if (cur == checker)
			return (1);
		cur = cur->next;
		checker = checker->next->next;
	}
	return (0);
}
