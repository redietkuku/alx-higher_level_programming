#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - displays byte info
 *
 * @p: is a python object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int the_size, x, the_limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	the_size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", the_size);
	printf("  trying string: %s\n", string);

	if (the_size >= 10)
		the_limit = 10;
	else
		the_limit = the_size + 1;

	printf("  first %ld bytes:", the_limit);

	for (x = 0; x < limit; x++)
		if (string[x] >= 0)
			printf(" %02x", string[x]);
		else
			printf(" %02x", 256 + string[x]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int the_size, x;
	PyListObject *list;
	PyObject *obj;

	the_size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", the_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < the_size; x++)
	{
		obj = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
