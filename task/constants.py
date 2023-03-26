class TASK:
        class STATUS:
                CONSTANTS = (
                        (0, 'Todo'),
                        (1, 'In process'),
                        (2, 'Done'),
                        (3, 'Cancelled'),
                )
                DEFAULT = 0

        class PRIORITY:
                CONSTANTS = (
                        (0, 'Lowest'),
                        (1, 'Low'),
                        (2, 'Medium'),
                        (3, 'High'),
                        (4, 'Highest'),
                    )
                DEFAULT = 2