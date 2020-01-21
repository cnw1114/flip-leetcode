# class Solution:
#     def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
#         dir_file_split = [item.split(' ') for item in paths]

#         file_dict = {}
#         for item in dir_file_split:
#             for file in item[1:]:
#                 if file in file_dict:
#                     file_dict[file].append(item[0])
#                 else:
#                     file_dict[file] = [item[0]]
#         print(file_dict)
#         contents_dict = {}
#         for file in file_dict.keys():
#             contents = file[file.index('(')+1:file.index(')')]
#             if contents in contents_dict:
#                 contents_dict[contents].append(file)
#             else:
#                 contents_dict[contents] = [file]
#         print(contents_dict)
#         output = []
#         for contents in contents_dict.keys():
#             same_contents = []
#             for file in contents_dict[contents]:
#                 for dir_ in file_dict[file]:
#                     same_contents.append(dir_+'/'+file[:file.index('(')])
#             if len(same_contents) == 1:
#                 continue
#             output.append(same_contents)
        
#         return output

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents_info = collections.defaultdict(lambda: [])
        ret  = []
        for path in paths:
            path = path.split(" ")
            path[0] += "/"
            for file in path[1:]:
                file, content = file.split("(")
                contents_info[content[:-1]].append(path[0] + file)

        for paths in contents_info.values():
            if (len(paths) >= 2):
                ret.append(paths)
                          
        return ret
