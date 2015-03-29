import urllib2
import os

def main():
    
    resources_dir_name = 'resources'
    
    # Create resources directory to save all resources to
    if not os.path.exists(resources_dir_name):
        os.mkdir(resources_dir_name)
    
    # Read file with links
    urls_file = open('resources_links.txt')
    urls = urls_file.readlines()
    
    # Read file with resources names
    files_names_file = open('resources_names.txt')
    names = files_names_file.readlines()
    
    for index, link in enumerate(urls):
        
        # Open link. Read contents
        page_response_obj = urllib2.urlopen(link)
        page_response = page_response_obj.read()
        
        # Write to a file with specified name.
        # In case it exists, overwrite it.
        # Strip removes newlines and whitespaces on sides.
        file_name = names[index].strip()
        file_name = os.path.join(resources_dir_name, file_name)
        new_file = open(file_name, 'w+')
        new_file.write(page_response)
        new_file.close()
        print "file {} was successfully saved".format(file_name)

if __name__ == '__main__':
    main()