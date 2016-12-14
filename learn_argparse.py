# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:
# Author:      jp $
# -------------------------------------------------------------------------------
import argparse


def use_process():
    parser = argparse.ArgumentParser()
    parser.parse_args()


def simple_example():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input_dir', type=str, default='/tmp', help='Directory to put the input data.')
    parser.add_argument('-o', '--output_file', type=str, default='/tmp/1.txt', help='File to store the output data.')
    parser.add_argument('-t', '--time', type=float, default='1.0', help='Min log time.')

    FLAGS, unparsed = parser.parse_known_args()

    print 'FLAGS=%s\nunparsed=%s' % (FLAGS, unparsed)
    print 'input_dir=%s\noutput_file=%s\ntime=%s' % (FLAGS.input_dir, FLAGS.output_file, FLAGS.time)

if __name__ == '__main__':
    pass
    # use_process()
    simple_example()




