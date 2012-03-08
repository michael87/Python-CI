from utils.versioning import Versioning
from svn import fs, repos, core

class Subversion(Versioning):
    
    #@todo: test
    def connect(self, repository):
        """
        Connect with repository
        
        @todo: Create validation for repository url
        """    
        
        self.repository = repos.open(repository)
        
        self.fs_ptr = repos.fs(self.repository)
        
    def get_actual_version(self):
        """
        Get the actual version of the repostory
        
        @return: youngest_rev
        """
        return fs.youngest_rev(self.fs_ptr)
    
    
    def get_revision_info(self, revision_number):
        """
        Get revision information:
        
        @return: svn_log, svn_date, svn_author
        """
        svn_log = fs.revision_prop(self.fs_ptr, revision_number, 'svn:log')
        
        svn_date = fs.revision_prop(self.fs_ptr, revision_number, 'svn:date')
        
        svn_author = fs.revision_prop(self.fs_ptr, revision_number, 'svn:author')
        
        return (svn_log, svn_date, svn_author)    
    