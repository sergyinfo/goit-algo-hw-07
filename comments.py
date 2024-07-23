class Comment:
    """Represents a single comment in a system with the capability of nesting replies."""

    def __init__(self, text: str, author: str):
        """
        Initializes the comment with text and author.

        Args:
            text: The text of the comment.
            author: The author of the comment.
        """
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, comment: 'Comment') -> None:
        """
        Adds a reply to this comment.

        Args:
            comment: The comment to add as a reply.
        """
        self.replies.append(comment)

    def remove_reply(self) -> None:
        """Marks the comment as deleted and changes its text to a generic message."""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level: int = 0) -> None:
        """
        Recursively displays this comment and all its replies with indentation to show hierarchy.

        Args:
            level: The current level of indentation.
        """
        # Display the current comment
        indent = "    " * level
        status_text = self.text if not self.is_deleted else "Цей коментар було видалено."
        print(f"{indent}{self.author}: {status_text}")
        
        # Recursively display each reply
        for reply in self.replies:
            reply.display(level + 1)

# Example of using the above implementation:

# Create the root comment and replies
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

# Add replies to the root comment
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# Create a reply to the first reply and add it
reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Remove the first reply
reply1.remove_reply()

# Display all comments and replies
root_comment.display()
