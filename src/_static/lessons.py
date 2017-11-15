import os
import urlparse
from models import courses
from controllers import sites
from controllers import utils


def append_lesson_content(from_lesson, to_lesson):
    """Append lesson properties from the send lesson to the receiving lesson """
    to_lesson.objectives = from_lesson.objectives
    to_lesson.activity_title = from_lesson.activity
    to_lesson.title = from_lesson.title
    to_lesson.notes = from_lesson.notes
    to_lesson.video = from_lesson.video
    to_lesson.activity_listed = from_lesson.activity_listed

    return to_lesson


def get_unit_lesson_id_from_url(url):
    """Extracts unit and lesson ids from a URL."""
    url_components = urlparse.urlparse(url)
    query_dict = urlparse.parse_qs(url_components.query)
    url_path = url_components.path
    path_list = url_path.split(os.sep)
    namespace = 'ns_{}'.format(path_list[1])

    if 'unit' not in query_dict:
        return None, None

    unit_id = query_dict['unit'][0]

    lesson_id = None
    if 'lesson' in query_dict:
        lesson_id = query_dict['lesson'][0]

    data_obj = {
        "unit_id": unit_id,
        "lesson_id": lesson_id,
        "namespace": namespace
    }

    return data_obj


class CopyLessonRESTHandler(utils.BaseHandler):
    """ Handler that handles the copy of lesson content from one course to another"""
    URL = '/lesson'

    def post(self):
        from_url = self.request.get("fromUrl")

        to_url = self.request.get("toUrl")

        from_course_data = get_unit_lesson_id_from_url(from_url)
        to_course_data = get_unit_lesson_id_from_url(to_url)
        from_context = sites.get_app_context_for_namespace(from_course_data['namespace'])

        if from_context:
            to_context = sites.get_app_context_for_namespace(to_course_data['namespace'])
        else:
            self.error(400)

        if to_context:
            from_course = courses.Course(None, app_context=from_context)

            receiving_course = courses.Course(None, app_context=to_context)

            sending_lesson = from_course.find_lesson_by_id(from_course_data["unit_id"],
                                                           from_course_data["lesson_id"])
            receiving_lesson = receiving_course.find_lesson_by_id(to_course_data["unit_id"],
                                                                  to_course_data["lesson_id"])

            if sending_lesson and receiving_lesson:

                new_lesson = append_lesson_content(sending_lesson, receiving_lesson)

                if new_lesson:
                    receiving_course.update_lesson(new_lesson)
                    receiving_course.save()

                return self.response
