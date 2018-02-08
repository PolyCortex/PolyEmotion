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
        private string currentDirectory = Directory.GetCurrentDirectory();
        private DirectoryInfo songsDirectory;

        public PlaylistControl()
        {
            InitializeComponent();
            DirectoryInfo songsDirectory = new DirectoryInfo(Directory.GetCurrentDirectory());
            getSongsDirectory();
            getSongs();
        }

        private void getSongs()
        {
            string[] files = Directory.GetFiles(songsDirectory.ToString());
            foreach (string file in files)
            {
                songPlaylist.Items.Add(Path.GetFileName(file));
            }
        }

        private void getSongsDirectory()
        {
            string[] dirs = Directory.GetDirectories(songsDirectory.ToString());
            while (!dirs.Contains("Songs"))
            {
                songsDirectory = Directory.GetParent(songsDirectory.ToString());
            }
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

        /*private void tabControl1_DrawItem(object sender, DrawItemEventArgs e)
        {
            Graphics g = e.Graphics;
            Brush _textBrush;

            // Get the item from the collection.
            TabPage _tabPage = tabControl1.TabPages[e.Index];
            
            // Get the real bounds for the tab rectangle.
            Rectangle _tabBounds = tabControl1.GetTabRect(e.Index);

            if (e.State == DrawItemState.Selected)
            {
                // Draw a different background color, and don't paint a focus rectangle.
                _textBrush = new SolidBrush(Color.Red);
                g.FillRectangle(Brushes.Gray, e.Bounds);
            }

            else
            {
                _textBrush = new System.Drawing.SolidBrush(e.ForeColor);
                e.DrawBackground();
            }

            // Use our own font.
            Font _tabFont = new Font("Arial", (float)10.0, FontStyle.Bold, GraphicsUnit.Pixel);

            // Draw string. Center the text.
            StringFormat _stringFlags = new StringFormat();
            _stringFlags.Alignment = StringAlignment.Center;
            _stringFlags.LineAlignment = StringAlignment.Center;
            g.DrawString(_tabPage.Text, _tabFont, _textBrush, _tabBounds, new StringFormat(_stringFlags));
        }*/
    }
}
