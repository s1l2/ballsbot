from ballsbot.utils import keep_rps, run_as_thread
from ballsbot_detection import ballsbot_detection


class Detector:
    def __init__(self):
        self.fps = 2
        self.objects_detected = None
        self.main_object_detected = None
        self.object_classes = {
            'cat': 3,
            'dog': 2,
            'person': 1,
        }

    def start(self):
        ballsbot_detection.startup_detection()
        ts = None
        while True:
            ts = keep_rps(ts, fps=self.fps)
            detections = ballsbot_detection.detect()
            detections = list(filter(lambda x: x['object_class'] in self.object_classes, detections))

            for an_object in detections:
                an_object['hsize'] = an_object['top_right'][0] - an_object['bottom_left'][0]
                an_object['vsize'] = an_object['top_right'][1] - an_object['bottom_left'][1]
                an_object['size'] = an_object['hsize'] * an_object['vsize']
                an_object['center'] = (
                    an_object['bottom_left'][0] + an_object['hsize'] / 2.,
                    an_object['bottom_left'][1] + an_object['vsize'] / 2.,
                )

            # add main object from prev frame if there is no object with this class in current
            objects_detected = detections.copy()
            if self.main_object_detected is not None:
                seen_classes = set([x['object_class'] for x in detections])
                if self.main_object_detected['object_class'] not in seen_classes \
                        and len(list(filter(lambda x: x['object_class'] == self.main_object_detected['object_class'],
                                            self.objects_detected))) != 0:
                    detections.append(self.main_object_detected)

            if len(detections) == 0:
                self.main_object_detected = None
            elif len(detections) == 1:
                self.main_object_detected = detections[0]
            else:
                # first select class by max wight
                # second select largest instance
                self.main_object_detected = list(sorted(
                    detections,
                    key=lambda x: (self.object_classes[x['object_class']], x['size']),
                    reverse=True
                ))[0]

            self.objects_detected = objects_detected

    def get_seen_object(self):
        if self.main_object_detected is None:
            return None
        else:
            return self.main_object_detected.copy()
