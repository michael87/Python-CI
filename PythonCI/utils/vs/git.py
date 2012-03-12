from git import *

class Git():
    
    def connect(self, repository):
        
        self.repository = Repo(repository)
    
    def get_actual_version(self):
        pass
    
    def get_revision_info(self, revision_number):
        """
        Get revision information:
        
        @return: svn_log, svn_date, svn_author
        """
        
        # Return turple with all information
        return (svn_log, svn_date, svn_author)    
    
    def checkout_revision(self, revision_number):
        
        pass
    
    def update_to_revision(self, revision_number):
        
        pass