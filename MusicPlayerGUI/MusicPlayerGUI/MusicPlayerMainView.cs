using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace MusicPlayerGUI
{
    public partial class MusicPlayerMainView : Form
    {
        private string currentDirectory = System.IO.Path.Combine(System.IO.Directory.GetCurrentDirectory(), "Songs");
        public MusicPlayerMainView()
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
            getSongs();
        }

        private void songPlaylist_SelectedIndexChanged(object sender, EventArgs e)
        {
            mediaPlayer.URL = System.IO.Path.Combine(currentDirectory, songPlaylist.SelectedItem.ToString());
            mediaPlayer.Ctlcontrols.play();
            
        }

        private void MusicPlayerMainView_Load(object sender, EventArgs e)
        {

        }
    }
}
