#include <Python.h>

/**
 * print_python_list_info - print python list info
 * @p: a pyobject list
 */
void print_python_list_info(PyObject *p)
{
	int s, alloc, x;
	PyObject obj;

	s = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", alloc);
	for (x = 0; x < s; x++)
	{
		printf("Element %d: ", x);
		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
