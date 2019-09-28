package Calc;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.LinkedList;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.WindowConstants;
import java.awt.Color;


	interface LabelConstant {
	    int LABELWIDTH = 200;
	}
	
	class MyLabel extends JLabel {
	    public MyLabel(){
	    	super("0",RIGHT);
	    	Dimension d = getSize();
	    	d.width = LabelConstant.LABELWIDTH;
	    	setSize(d);
	    }
	    public ActionListener getActionListener(){
	    	return (event)->setText(event.getActionCommand());
	    }
	}
	
	interface FrameConstant {
	    int WIDTH = 500;
	    int HEIGHT = 400;
	    String TITLE = "計算機";
	}
	
	class MyFrame extends JFrame {
	    public void setCloseActionListener(ActionListener a){
		closeActionList.add(a);
	    }
	    
	    private final LinkedList<ActionListener> closeActionList
		= new LinkedList<ActionListener>();
	    class MyWindowListener extends WindowAdapter {
	        @Override
	        public void windowClosed(WindowEvent e){
	        	for(ActionListener listener : closeActionList){
	        		listener.actionPerformed(
	                   new ActionEvent(
	                     this,ActionEvent.ACTION_PERFORMED,"close"));
	        	}
	        }
	    }
	    
	    public MyFrame(){
	        super();    
	        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
	        addWindowListener(new MyWindowListener());
	        setSize(FrameConstant.WIDTH,FrameConstant.HEIGHT);
	        setTitle(FrameConstant.TITLE);
	    }
	}
	
	class Main {
	    public static void main(String[] arg) throws ParseException {
	    	final MyFrame frame = new MyFrame();
	    	final Keyboard keyboard = new Keyboard();
	    	frame.setCloseActionListener(keyboard.getCloseAction());
	    	
	    	final Container container = frame.getContentPane();
	    	container.add(keyboard.getPanel(), BorderLayout.CENTER);
	    	
	    	final MyLabel label = new MyLabel();
	    	label.setOpaque(true);
	    	label.setFont(new Font("Arial", Font.PLAIN, 50));
	    	label.setPreferredSize(new Dimension(100, 100));
	    	label.setBackground(new Color(245, 245, 245));
	    	
	    	container.add(label,BorderLayout.NORTH);
	    	frame.setVisible(true);
	    	Parser parser = new Parser(keyboard);
	    	parser.setActionListener(label.getActionListener());
	    	parser.start();
	    }
	}


