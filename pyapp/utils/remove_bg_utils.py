from removebg import RemoveBg


def remove_bg(input_path, API_KEY):
    # print(input_path)
    rmbg = RemoveBg(API_KEY, "error.log")
    rmbg.remove_background_from_img_file(input_path)
    return True