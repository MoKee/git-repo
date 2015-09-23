#
# Copyright (C) 2015 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import os
import shutil
import sys

from command import Command, RequiresGitcCommand
import gitc_utils

class GitcDestroy(Command, RequiresGitcCommand):
  common = True
  helpSummary = "Destroy a GITC Client."
  helpUsage = """
%prog
"""
  helpDescription = """
This subcommand destroys the current GITC client, deleting the GITC manifest
and all locally downloaded sources.
"""

  def _Options(self, p):
    p.add_option('-f', '--force',
                 dest='force', action='store_true',
                 help='Force the deletion (no prompt).')

  def Execute(self, opt, args):
    #client_name, gitc_client_dir = gitc_utils.parse_clientdir_info(os.getcwd())
    if not self.gitc_manifest:
      print('error: This command must be run in a GITC client.')
      sys.exit(1)
    if not opt.force:
      prompt = ('This will delete GITC client: %s\nAre you sure? (yes/no) ' %
                self.gitc_manifest.gitc_client_name)
      response = raw_input(prompt).lower()
      if not response == 'yes':
        print('Response was not "yes"\n Exiting...')
        sys.exit(1)
    shutil.rmtree(self.gitc_manifest.gitc_client_dir)
