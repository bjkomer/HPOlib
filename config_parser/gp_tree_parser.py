##
# wrapping: A program making it easy to use hyperparameter
# optimization software.
# Copyright (C) 2013 Katharina Eggensperger and Matthias Feurer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

import ConfigParser


def add_default(config):
    # This module reads gp_treeDefault.cfg and adds this defaults to a given config
    assert isinstance(config, ConfigParser.RawConfigParser), \
        "config is not a valid instance"

    config_fn = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "gp_treeDefault.cfg")
    if not os.path.isfile(config_fn):
        raise Exception('%s is not a valid file\n' % config_fn)

    gp_tree_config = ConfigParser.SafeConfigParser(allow_no_value=True)
    gp_tree_config.read(config_fn)
    # --------------------------------------------------------------------------
    # GP_TREE
    # --------------------------------------------------------------------------
    # Set default for GP_TREE
    if not config.has_section('GP_TREE'):
        config.add_section('GP_TREE')

    # optional cases
    if not config.has_option('GP_TREE', 'space'):
            config.set('GP_TREE', 'space',
                       gp_tree_config.get('GP_TREE', 'space'))

    if not config.has_option('GP_TREE', 'numberEvals'):
            config.set('GP_TREE', 'numberEvals',
                       config.get('DEFAULT', 'numberOfJobs'))
    return config
