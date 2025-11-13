from abc import ABC, abstractmethod

from encodings.punycode import selective_find


class IEmail(ABC):
	@abstractmethod
	def set_sender(self, sender):
		pass
	
	@abstractmethod
	def set_receiver(self, receiver):
		pass
	
	@abstractmethod
	def set_content(self, content):
		pass


class Email(IEmail):
	def __init__(self, protocol):
		self.protocol = protocol
		self.__sender = None
		self.__receiver = None
		self.__content = None
	
	def set_sender(self, sender):
		if self.protocol == 'IM':
			self.__sender = ''.join(["I'm ", sender])
		else:
			self.__sender = sender
	
	def set_receiver(self, receiver):
		if self.protocol == 'IM':
			self.__receiver = ''.join(["I'm ", receiver])
		else:
			self.__receiver = receiver
	
	def set_content(self, content):
		self.__content = content.format_content()
	
	def __repr__(self):
		return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


class IContent(ABC):
	def __init__(self, txt):
		self.txt = txt
	
	@abstractmethod
	def format_content(self):
		pass


class MyContent(IContent):
	def format_content(self):
		return f'<myML>{self.txt}</myML>'


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
