#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_loop - a function that create an infinite loop
 * with a sleep of 1 second in each iteration.
 *
 * Return: 0 on success.
 */
int infinite_loop(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point.
 *
 * Return: 0 on success.
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
		perror("Error creating child process");
		return (1);
		}
		if (child_pid == 0)
		{
		printf("Zombie process created, PID: %d\n", getpid());
		return (0);
		}
	}

	infinite_loop();

	return (0);
}
