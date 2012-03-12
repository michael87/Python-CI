from utils.versioning import Versioning
from svn import fs, repos, core

class Subversion(Versioning):
    
    #@todo: test
    def connect(self, repository):
        """
        Connect with repository
        
        @todo: Create validation for repository url
        """    
        
        # Open repository connection
        self.repository = repos.open(repository)
        self.fs_ptr = repos.fs(self.repository)
        
    def get_actual_version(self):
        """
        Get the actual version of the repostory
        
        @return: youngest_rev
        """
        
        # Return youngest revision
        return fs.youngest_rev(self.fs_ptr)
    
    
    def get_revision_info(self, revision_number):
        """
        Get revision information:
        
        @return: svn_log, svn_date, svn_author
        """
        
        # Get svn log information
        svn_log = fs.revision_prop(self.fs_ptr, revision_number, 'svn:log')
        
        # Commit date of the selected revision
        svn_date = fs.revision_prop(self.fs_ptr, revision_number, 'svn:date')
        
        # Author of the selected revisision
        svn_author = fs.revision_prop(self.fs_ptr, revision_number, 'svn:author')
        
        # Return turple with all information
        return (svn_log, svn_date, svn_author)    
    
    
    def checkout_revision(self, revision_number):
        
        pass
    
    def update_to_revision(self, revision_number):
        
        pass