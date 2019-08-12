from abc import ABC, abstractmethod
import numpy as np
import cv2

class BlobDetectionStrategy(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def detect_blobs(self):
        pass

class OpenCV_Simple_BlobDetectionStrategy(BlobDetectionStrategy):
    def _remove_noise(self, foreground_mask):
        '''
        Uses OpenCV morphological transformations to make blobs more defined
        Returns a foreground mask with more defined blobs
        '''
        erosion_kernel = np.ones(self.config['erosion_kernel'], np.uint8)
        dilation_kernel = np.ones(self.config['dilation_kernel'], np.uint8)

        foreground_mask = cv2.erode(foreground_mask, erosion_kernel, iterations = self.config['erosion_iterations'])
        foreground_mask = cv2.dilate(foreground_mask, dilation_kernel, iterations = self.config['dilation_iterations'])

        return foreground_mask

    def detect_blobs(self, foreground_mask):
        '''
        Detect and returns locations of blobs from foreground mask
        Returns list of coordinates
        '''
        # Morphological operations
        foreground_mask = self._remove_noise(foreground_mask)

        # Create a detector with the parameters
        detector = cv2.SimpleBlobDetector_create(self.config['blob_det_params'])

        # DETECT BLOBS

        #invert image (blob detection only works with white background)
        foreground_mask = cv2.bitwise_not(foreground_mask)

        # apply blur
        foreground_mask = cv2.blur(foreground_mask, self.config['blur_kernel'])

        return detector.detect(foreground_mask)

blob_detection_strategies = {
    'opencv': OpenCV_Simple_BlobDetectionStrategy
}