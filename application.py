from flask import Flask, render_template, request
import config
import aicontent

def page_not_found(e):
  return render_template('404.html'), 404


application = Flask(__name__)
application.config.from_object(config.config['development'])
application.register_error_handler(404, page_not_found)


@application.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        submission = request.form['jobDescription']
        skills = request.form['skills']
        # query = "List at least 10 work experience for a {} which includes these technical skills: {}".format(submission, skills)
        query = "List at least 5 work experience for a {} which includes these technical skills: {} for a resume.".format(submission, skills)

        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        # openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        openAIAnswer = openAIAnswerUnformatted.replace('\t', '<br>')
        prompt = 'Our suggestions for {} are:'.format(submission)

    return render_template('index.html', **locals())



# @app.route('/job-description', methods=["GET", "POST"])



if __name__ == '__main__':
    application.run(host='0.0.0.0', port='8888', debug=True)
