#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - prints basic info about lists in python
 * @p: PyObject
 *
 * Return: it returns nothing
 */
void print_python_list_info(PyObject *p)
{
PyObject *item;
PyListObject *list = (PyListObject *)p;
int x, the_size, alloc;

the_size = Py_SIZE(p);
alloc = list->allocated;
printf("[*] Size of the Python List = %d\n", the_size);
printf("[*] Allocated = %d\n", alloc);

for (x = 0; x < size; x++)
{
item =  PyList_GetItem(p, x);
printf("Element %d: %s\n", x, Py_TYPE(item)->tp_name);
}
}
