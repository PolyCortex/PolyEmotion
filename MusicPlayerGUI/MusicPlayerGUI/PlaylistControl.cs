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
        private string songsDirectory = Directory.GetCurrentDirectory();

        public PlaylistControl()
        {
            InitializeComponent();
            getSongsDirectory();
            getSongs();
        }

        private void getSongs()
        {
            string[] files = Directory.GetFiles(songsDirectory, "*.mp3");
            foreach (string file in files)
            {
                songPlaylist.Items.Add(Path.GetFileName(file));
            }
        }

        private void getSongsDirectory()
        {
            string[] dirs = Directory.GetDirectories(songsDirectory);
            while (!dirs.Contains(Path.Combine(songsDirectory, "Songs")))
            {
                songsDirectory = Directory.GetParent(songsDirectory).ToString();
                dirs = Directory.GetDirectories(songsDirectory);
            }

            songsDirectory = Path.Combine(songsDirectory, "Songs");
        }

        private void btnUpdatePlaylist_Click(object sender, EventArgs e)
        {
            songPlaylist.Items.Clear();
            getSongs();
        }

        private void songPlaylist_SelectedIndexChanged(object sender, EventArgs e)
        {
            mediaPlayer.URL = Path.Combine(songsDirectory.ToString(), songPlaylist.SelectedItem.ToString());
            mediaPlayer.Ctlcontrols.play();
        }
    }
}
