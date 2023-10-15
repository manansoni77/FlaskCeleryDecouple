from worker import worker

print('Application started')

numTasks = 100
tasks = []

if __name__ == '__main__':
    for i in range(numTasks):
        tasks.append(
            worker.send_task('addTask', (i, 3))  # Send task by name
        )
        print('Sent task:', i)

    for task in tasks:
        result = task.get()
        print('Received result:', result)

    print('Application ended')