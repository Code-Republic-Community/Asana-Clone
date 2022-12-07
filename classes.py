class User:
    def __init__(self, user_name, email, password, phone):
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__phone = phone

    def set_username(self, new_name):
        self.__user_name = new_name

    def set_email(self, new_email):
        self.__email = new_email

    def set_password(self, new_password):
        self.__password = new_password

    def set_phone(self, new_phone):
        self.__phone = new_phone


class Projects:
    def __init__(self, project_name, privacy):
        self.__project_name = project_name
        self.__privacy = privacy

    def get_project_name(self):
        return self.__project_name

    def set_project_name(self, new_project_name):
        self.__project_name = new_project_name

    def get_privacy(self):
        return self.__privacy

    def set_privacy(self,new_privacy):
        self.__privacy = new_privacy


class Section:
    def __init__(self, sect_name):
        self.__sect_name = sect_name

    def rename_sect(self, new_sect_name):
        self.__sect_name = new_sect_name


class Task:
    def __init__(self, task_name = 'Untitled'):
        self.__task_name = task_name
        self.__assignee = None
        self.__due_date = None
        self.__description = None
        self.__comment = None

    def set_task_name(self, new_name):
        self.__task_name = new_name

    def get_task_name(self):
        return self.__task_name

    def set_assignee(self, new_assignee):
        self.__assignee = new_assignee

    def get_assignee(self):
        return self.__assignee

    def set_due_date(self, new_due_date):
        self.__due_date = new_due_date

    def get_due_date(self):
        return self.__due_date

    def set_description(self, text):
        self.__description = text

    def get_description(self):
        return self.__description

    def set_comment(self, text):
        self.__comment = text

    def get_comment(self):
        return self.__comment


class Subtask(Task):
    def __init__(self, parent: Task):
        super().__init__()
        self.__parent = parent

    def get_parent(self):
        return self.__parent


class Members:
    def __init__(self, member_name: User):
        self.__member_name = member_name

    def get_member_name(self):
        return self.__member_name

    def select_member(self):
        pass


class Message:
    def __init__(self, who: User, id, whom: User):
        self.__who = who
        self.__whom = whom
        self.__id = id
        self.__date = None
        self.__text = ""

    def edit(self, new_text):
        self.__text = new_text
        return self.__text

    def send(self):
        pass

    def set_who(self, who: User):
        self.__who = who




