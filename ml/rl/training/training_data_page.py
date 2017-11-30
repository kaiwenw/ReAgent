#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np


class TrainingDataPage(object):
    __slots__ = [
        'states', 'actions', 'rewards', 'next_states',
        'next_actions', 'possible_next_actions', 'reward_timelines', 'ds',
        'not_terminals'
    ]

    def __init__(
        self, states, actions, rewards, next_states, next_actions,
        possible_next_actions: np.ndarray, reward_timelines, ds,
        not_terminals=None
    ) -> None:
        """
        Creates a TrainingDataPage object.

        In the case where `not_terminals` can be determined by next_actions or
        possible_next_actions, feel free to omit it.
        """
        self.states = states
        self.actions = actions
        self.rewards = rewards
        self.next_states = next_states
        self.next_actions = next_actions
        self.possible_next_actions = possible_next_actions
        self.reward_timelines = reward_timelines
        self.ds = ds
        self.not_terminals = not_terminals
