from depthai_sdk import OakCamera
import depthai as dai # type: ignore

with OakCamera() as oak:
    color = oak.create_camera('color')
    # List of models that are supported out-of-the-box by the SDK:
    # https://docs.luxonis.com/projects/sdk/en/latest/features/ai_models/#sdk-supported-models
    nn = oak.create_nn('yolo-v3-tf', color, spatial=True, tracker=True)

    nn.config_tracker(
        tracker_type=dai.TrackerType.ZERO_TERM_COLOR_HISTOGRAM,
        track_labels=[0], # Track only 1st object from the object map. If unspecified, track all object types
        # track_labels=['person'] # Track only people (for coco datasets, person is 1st object in the map)
        assignment_policy=dai.TrackerIdAssignmentPolicy.SMALLEST_ID,
        max_obj=10, # Max objects to track, which can improve performance
        threshold=0.1 # Tracker threshold
    )
    nn.config_spatial(
        bb_scale_factor=0.5, # Scaling bounding box before averaging the depth in that ROI
        lower_threshold=300, # Discard depth points below 30cm
        upper_threshold=10000, # Discard depth pints above 10m
        # Average depth points before calculating X and Y spatial coordinates:
        calc_algo=dai.SpatialLocationCalculatorAlgorithm.AVERAGE
    )

    oak.visualize(nn.out.main, fps=True)
    oak.visualize([nn.out.passthrough, nn.out.spatials])
    oak.start(blocking=True)