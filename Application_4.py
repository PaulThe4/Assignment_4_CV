from flask import Flask, render_template, Response # type: ignore
from depthai_sdk import OakCamera
import depthai as dai # type: ignore

app = Flask(__name__)

# Function to start the camera and capture frames
def generate_frames():
    with OakCamera() as oak:
        color = oak.create_camera('color')
        nn = oak.create_nn('yolo-v3-tf', color, spatial=True, tracker=True)

        nn.config_tracker(
            tracker_type=dai.TrackerType.ZERO_TERM_COLOR_HISTOGRAM,
            track_labels=[0],
            assignment_policy=dai.TrackerIdAssignmentPolicy.SMALLEST_ID,
            max_obj=10,
            threshold=0.1
        )

        nn.config_spatial(
            bb_scale_factor=0.5,
            lower_threshold=300,
            upper_threshold=10000,
            calc_algo=dai.SpatialLocationCalculatorAlgorithm.AVERAGE
        )

        oak.visualize(nn.out.main, fps=True)
        oak.visualize([nn.out.passthrough, nn.out.spatials])

        oak.start(blocking=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)