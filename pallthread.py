import threading as th


class PallThread(th.Thread):

	stop_request = th.Event()

	def run(self):
		pass

	def stop(self):
		self.stop_request.set()
		if self.is_alive:
			self.join()
