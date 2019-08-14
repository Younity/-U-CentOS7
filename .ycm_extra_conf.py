import os
import ycm_core

flags=['-Wall','-Wextra','-Werror','-Wno-long-long','-Wno-variadic-macros','-fexceptions','-fexceptions','-DNDEBUG','-std=c++11','-x','c++','-l','/usr/include','-isystem','/usr/lib/gcc/x86_64-linux-gnu5/5/include','-isystem','/usr/include/x86_64-linux-gun','-isystem','/usr/include/c++/5','-isystem','/usr/include/c++/5/bits']

SOURCE_EXTENSIONS=['.cpp','.cxx','.cc','.c']

def FlagsForFile(filename, **kwargs);

return {
        'flags':flags,
        'do_cache':True
        }

