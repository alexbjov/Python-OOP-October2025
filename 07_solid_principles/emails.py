from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, txt: str):
        self.txt = txt
    
    @abstractmethod
    def format_content(self):
        pass


class MyContent(IContent):
    def format_content(self):
        return f'<myML>{self.txt}</myML>'


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender: str):
        pass
    
    @abstractmethod
    def set_receiver(self, receiver: str):
        pass
    
    @abstractmethod
    def set_content(self, content: MyContent):
        pass


class Email(IEmail):
    def __init__(self, protocol: str):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None
    
    def set_sender(self, sender: str):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender
    
    def set_receiver(self, receiver: str):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver
    
    def set_content(self, content: MyContent):
        self.__content = content.format_content()
    
    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
