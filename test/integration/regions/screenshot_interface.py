from pypom import Page

class ScreenshotInterface(Page):

    @property
    def loaded(self):
        return 'https://www.mozilla.org' in self.selenium.current_url

    @property
    def door_hanger(self):
        from door_hanger import DoorHanger
        return DoorHanger(self)

    @property
    def onboarding(self):
        from onboarding import Onboarding
        return Onboarding(self)

    @property
    def preselection(self):
        from selection import PreSelection
        return PreSelection(self)

    @property
    def selection(self):
        from selection import Selection
        return Selection(self)

