import os


def cont_file_and_dir(params_dir):

    """
        get the change data from 

    """
    file_cont = 0
    dir_cont = 0
    file_names = []
    dir_names = []

    for entry in os.listdir(params_dir):

        complete_path = os.path.join(params_dir, entry)

        if os.path.isfile(complete_path):
            file_cont += 1
            file_names.append(entry)
        elif os.path.isdir(complete_path):
            dir_cont +=1
            dir_names.append(entry)

    return file_cont, dir_cont, file_names, dir_names

def change_file_names(params_dir):

    # Generate the name of a sequence
    operating_cond = "operating_condtion_iter"
    file_cont, dir_cont, file_names, dir_names =  cont_file_and_dir(params_dir)
    seqence_operating_cond = [operating_cond + "_" +str(i) + ".txt" for i in range(file_cont)]
    for idx, filename in enumerate(file_names):
        old_name  =os.path.join(params_dir, filename)
        new_name = os.path.join(params_dir, seqence_operating_cond[idx])
        os.rename(old_name, new_name)

    return new_name