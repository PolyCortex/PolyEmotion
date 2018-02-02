using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace MusicPlayerGUI
{
    public partial class PlaylistControl : UserControl
    {
        private string currentDirectory = System.IO.Path.Combine(System.IO.Directory.GetCurrentDirectory(), "Songs");

        public PlaylistControl()
        {
            InitializeComponent();
            getSongs();
        }

        private void getSongs()
        {
            string[] files = System.IO.Directory.GetFiles(currentDirectory);
            foreach (string file in files)
            {
                songPlaylist.Items.Add(System.IO.Path.GetFileName(file));
            }
        }
        private void btnUpdatePlaylist_Click(object sender, EventArgs e)
        {
            songPlaylist.Items.Clear();
            getSongs();
        }

        private void songPlaylist_SelectedIndexChanged(object sender, EventArgs e)
        {
            mediaPlayer.URL = System.IO.Path.Combine(currentDirectory, songPlaylist.SelectedItem.ToString());
            mediaPlayer.Ctlcontrols.play();
        }
    }
}
