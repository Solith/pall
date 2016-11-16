
import logging

from pallthread import PallThread


LOGGER = logging.getLogger(__name__)

class Pall(object):

	_threads = None

	def __init__(self):
		self._threads = {}

	def __del__(self):
		for thr in self._threads:
			LOGGER.warning("Stopping leftover threads: {}".format(thr))
			if self._threads[thr].is_alive():
				self._threads[thr].stop()
			del self._threads[thr]

	def new_thread(self, target, name):
		""" Get new thread.

		@param Runnable target: Method to be used as run(). Must use
		                        self.stop_request event.
		@param string name: Name for the thread. Must be unique.
		@returns Thread: The new thread.
		@raises RuntimeError: If thread with such name already exists.
		"""
		PallThread.run = target
		pallthr = PallThread()
		if name in self._threads:
			msg = "Thread named {} already exists".format(name)
			LOGGER.error(msg)
			raise RuntimeError(msg)
		else:
			self._threads[name] = pallthr
			return pallthr

	def stop_thread(self, name):
		""" Stop the name thread.

		@param string name: Name for the thread. Must be unique.
		@raises RuntimeError: If thread with such name already exists.
		"""
		if not name in self._threads:
			msg = "No thread named {} exists".format(name)
			LOGGER.error(msg)
			raise RuntimeError(msg)
		self._threads[name].stop()
		del self._threads[name]

	def exists(self, name):
		""" Check if name already exists.

		@param string name: Name for the thread.
		"""
		return name in self._threads.keys()
