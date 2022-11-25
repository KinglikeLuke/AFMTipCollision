class PID:
    def __init__(self, p_const, t_i, t_d):
        self.p_const = p_const
        self.t_i = t_i
        self.t_d = t_d
        self.prev_feedback = 0  # initiate storage for older feedback values
        self.cumm_feedback = 0

    def control(self, feedback):
        p = feedback
        d = feedback - self.prev_feedback
        i = feedback + self.cumm_feedback
        self.prev_feedback = feedback
        self.cumm_feedback += feedback

        output = self.p_const*p + self.p_const*self.t_i*i + self.p_const*self.t_d*d
        return output



