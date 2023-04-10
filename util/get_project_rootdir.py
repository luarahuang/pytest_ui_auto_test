import pytest

class GetProjectRootdir:
    def project_rootdir(self):
        return pytest.Config.rootpath
    

if __name__ == '__main__':
    rootdir = GetProjectRootdir().project_rootdir()
    print(rootdir)